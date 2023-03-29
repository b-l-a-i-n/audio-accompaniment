from deep_translator import GoogleTranslator
from PIL import Image
import loaded_models
import torch
import io

loaded_models.init()

def detect_objects(image: Image):
    inputs = loaded_models.processor(images=image, return_tensors="pt")
    outputs = loaded_models.detection_model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = loaded_models.processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.7)[0]

    detected_objects = []

    for label in results["labels"]:
        det_obj = loaded_models.detection_model.config.id2label[label.item()]
        if det_obj not in detected_objects:
            detected_objects.append(det_obj)
    
    return detected_objects

def translate(text_items: list):
    translator = GoogleTranslator(source='en', target='ru')
    return [translator.translate(i) for i in text_items]

def predict_text_from_image(image: Image):

    max_length = 16
    num_beams = 4
    gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

    images = [image]

    pixel_values = loaded_models.feature_extractor(images=images, return_tensors="pt").pixel_values

    output_ids = loaded_models.model.generate(pixel_values, **gen_kwargs)

    preds = loaded_models.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]

    return preds

def union_text(predicted_text, detected_objects):
    start_text = 'В текущей сцене: '
    middle_text = '. Тем временем вокруг: '
    result = start_text + predicted_text[0] + middle_text + ", ".join(detected_objects) + '.'
    return result


async def process_file_from_server(file):
    """
    :file: Binary image
    :return: json with predicted values
    """
    request_object_content = await file.read()
    image = Image.open(io.BytesIO(request_object_content))
    if image.mode != "RGB":
      image = image.convert(mode="RGB")

    predictions = predict_text_from_image(image)
    predictions = translate(predictions)

    detected_objects = detect_objects(image)
    detected_objects = translate(detected_objects)

    result_text = union_text(predictions, detected_objects)

    return {
        "predictions": result_text
    }