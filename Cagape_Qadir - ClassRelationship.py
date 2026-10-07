class Machine:
    def __init__(self, serial_number):
        self.serial_number = serial_number 
        
    def show_info(self): 
        print(f"Machine Serial Number: {self.serial_number}") 

class DeliveryRobot(Machine): 
    def __init__(self, serial_number, cargo_capacity): 
        super().__init__(serial_number) 
        self.cargo_capacity = cargo_capacity 
        self.control_board = ControlBoard() 
        
    def show_info(self): 
        super().show_info() 
        print(f"Cargo Capacity: {self.cargo_capacity} kg") 

class ControlBoard: 
    def __init__(self): 
        pass 

class RoboticsRoom: 
    def __init__(self, delivery_robot): 
        self.delivery_robot = delivery_robot 

class DiagnosticTool: 
    def __init__(self): 
        pass 

class Technician: 
    def __init__(self): 
        pass 
        
    def inspect_robot(self, diagnostic_tool): 
        print("Technician is inspecting the robot using the diagnostic tool.")


delivery_robot1 = DeliveryRobot("Mr. Robot", 50) 
delivery_robot1.show_info() 

robotics_room = RoboticsRoom(delivery_robot1) 
del robotics_room 
print("Robotics Room deleted. The Delivery Robot still exists.") 

diagnostic_tool = DiagnosticTool() 
technician = Technician() 
technician.inspect_robot(diagnostic_tool) 
print("Technician inspection completed. The Delivery Robot and Control Board still exist.")
