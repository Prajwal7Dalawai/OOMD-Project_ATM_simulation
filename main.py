from model.atm_model import ATMModel
from view.atm_view import ATMView
from controller.atm_controller import ATMController

def main():
    # Create MVC components
    model = ATMModel()
    controller = ATMController(model, None)  # Create controller first
    view = ATMView(controller)  # Pass controller to view
    controller.view = view  # Set view in controller

    # Start the application
    view.run()

if __name__ == "__main__":
    main() 