""" 
[Factory Design Pattern] Build a logging system using the 
Factory Design Pattern. 
Create a LoggerFactory class that generates different 
types of loggers (e.g., FileLogger, ConsoleLogger,
DatabaseLogger). Implement methods in each logger 
to write logs to their respective destinations. 
Show how the Factory Design Pattern helps to decouple 
the logging system from the application and 
allows for flexible log handling.
"""
import sqlite3 
import datetime 


class Logger:
    def log(self, message):
        pass 


class FileLogger(Logger):
    def log(self, message):
        with open('file_log.txt', 'a') as file:
            file.write(f"File logger has logged {message}\n")


class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console logger has logged {message}\n")


class DatabaseLogger(Logger):
    def log(self, message):
        self.connection = sqlite3.connect("db_logs.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Logs
                            (id INTEGER PRIMARY KEY,
                            timestamp TIMESTAMP,
                            message TEXT)"""
        )
        self.connection.commit()
        time_ = datetime.datetime.now()
        self.cursor.execute(
            "INSERT INTO Logs (timestamp, message) VALUES (?, ?)", (message, time_)
        )
        self.connection.commit()
        print(f'Database Logger has logged {message}\n')
        print(self.cursor.execute("SELECT * FROM Logs").fetchall())


class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "database":
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type")


logger_factory = LoggerFactory()

file_logger = logger_factory.get_logger("file")
console_logger = logger_factory.get_logger("console")
database_logger = logger_factory.get_logger("database")

file_logger.log("This is a log message written to a file.")
console_logger.log("This is a log message printed to the console.")
database_logger.log("This is a log message stored in the database.")