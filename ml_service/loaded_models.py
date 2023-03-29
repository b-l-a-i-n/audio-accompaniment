from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, DetrImageProcessor, DetrForObjectDetection
import torch

def init():
    global model, feature_extractor, tokenizer, processor, detection_model

    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
    detection_model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model.to(device)
    detection_model.to(device)