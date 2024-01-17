import pandas as pd

class Data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            self.df = None

    def display_data(self):
        print("Current Data:")
        print(self.df)

    def add_data(self):
        new_data = {}
        print("Enter new data:")
        for column in self.df.columns:
            new_data[column] = [input(f"Enter {column}: ")]
        self.df = pd.concat([self.df, pd.DataFrame(new_data)], ignore_index=True)
        self.df.to_csv(self.file_path, index=False)
        print("New data added successfully.")

    def calculate_statistics(self):
        print("Mean Values:")
        print(self.df.mean(numeric_only=True))
        print("\nMedian Values:")
        print(self.df.median(numeric_only=True))

    def filter_by_price(self):
        try:
            threshold = float(input("Enter the price threshold: "))
            if 'Price' in self.df.columns:
                filtered_df = self.df[self.df['Price'] > threshold]
                print(filtered_df)
            else:
                print("Column 'Price' not found in the DataFrame.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def filter_by_category(self):
        category = input("Enter the category to filter by (Electronics, Clothing, Books, Home Decor): ")
        filtered_df = self.df[self.df['Category'] == category]
        print(filtered_df)

    def edit_data(self):
        self.display_data()
        try:
            row_index = int(input("Enter the index of the row you want to edit: "))
            if 0 <= row_index < len(self.df):
                print("Enter new values:")
                for column in self.df.columns:
                    new_value = input(f"Enter new {column}: ")
                    self.df.at[row_index, column] = new_value
                self.df.to_csv(self.file_path, index=False)
                print("Data edited successfully.")
            else:
                print("Invalid row index.")
        except ValueError:
            print("Invalid input. Please enter a valid row index.")

    def delete_data(self):
        self.display_data()
        try:
            row_index = int(input("Enter the index of the row you want to delete: "))
            if 0 <= row_index < len(self.df):
                self.df = self.df.drop(index=row_index).reset_index(drop=True)
                self.df.to_csv(self.file_path, index=False)
                print("Data deleted successfully.")
            else:
                print("Invalid row index.")
        except ValueError:
            print("Invalid input. Please enter a valid row index.")

class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance.data = None
        return cls._instance

    def set_data(self, data):
        self.data = data

class AppDriver:
    def __init__(self):
        self.data_manager = DataManager()

    def run(self):
        file_path = 'C:/Users/KAVYA/github-classroom/SPM/-ACS_567_HWK-repository/ACS_567_HWK/data.csv'
        self.data_manager.set_data(Data(file_path))

        while True:
            print("\nMenu:")
            print("1. Display Data")
            print("2. Add Data")
            print("3. Calculate Mean and Median")
            print("4. Filter by Price")
            print("5. Filter by Product Category")
            print("6. Edit Data")
            print("7. Delete Data")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.data_manager.data.display_data()
            elif choice == '2':
                self.data_manager.data.add_data()
            elif choice == '3':
                self.data_manager.data.calculate_statistics()
            elif choice == '4':
                self.data_manager.data.filter_by_price()
            elif choice == '5':
                self.data_manager.data.filter_by_category()
            elif choice == '6':
                self.data_manager.data.edit_data()
            elif choice == '7':
                self.data_manager.data.delete_data()
            elif choice == '8':
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    app = AppDriver()
    app.run()




