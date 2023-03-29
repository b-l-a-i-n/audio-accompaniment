// Не хочет тут импортироваться

export class AccessButton extends shaka.ui.Element{
    constructor(parent, controls) {
        super(parent, controls);


        this.button_ = document.createElement('button');
        this.button_.textContent = 'Enable accessibility features';
        this.button_.setAttribute('aria-label', 'Accessibility');
        this.button_.classList.add('shaka-overflow-button');
        this.button_.classList.add('shaka-tooltip-status');
        this.button_.setAttribute("aria-label", "Accessibility");
        this.button_.setAttribute("id", "accessibilityButton");
        this.parent.appendChild(this.button_);

    }

};

AccessButton.Factory = class {
    create(rootElement, controls) {
        return new AccessButton(rootElement, controls);
    }
};
shaka.ui.Controls.registerElement('accessibility', new AccessButton.Factory());


