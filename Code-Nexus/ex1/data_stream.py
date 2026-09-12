from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.internal_storage: list[str] = []
        self.rank_counter = 0
        self.total_count = 0
        self.name = ""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        current_rank = self.rank_counter
        try:
            current_storage = self.internal_storage.pop(0)
        except IndexError:
            current_storage = ""
        return (current_rank, current_storage)


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        print(f"Registering {proc.name} Processor\n")
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        all_are_valid = False
        try:
            for data in stream:
                check = False
                for proc in self.processors:
                    if proc.validate(data):
                        proc.ingest(data)
                        check = True
                        all_are_valid = True
                        break
                if not check:
                    print(f"DataStream error - Can’t process \
element in stream : {data}")
            if not all_are_valid:
                print("no data processor can handle an element")
        except TypeError as e:
            print(e)

    def print_processors_stats(self) -> None:
        if len(self.processors) == 0:
            print("No processor found, no data\n")
        else:
            for proc in self.processors:
                print(f"{proc.name} : total {proc.total_count} \
items processed, remaining {len(proc.internal_storage)} on processor")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
                else:
                    pass
        elif isinstance(data, (int, float)):
            return True
        else:
            return False
        return True

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) is False:
            print(f"Test invalid ingestion of string \
'{data}' without prior validation:")
            raise TypeError("Got exception: Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.internal_storage.append(str(item))
                self.total_count += 1
        else:
            self.internal_storage.append(str(data))
            self.total_count += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
                else:
                    pass
        elif isinstance(data, str):
            return True
        else:
            return False
        return True

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is False:
            print(f"Test invalid ingestion of string \
'{data}' without prior validation:")
            raise TypeError("Got exception: Improper text data")
        if isinstance(data, list):
            for item in data:
                self.internal_storage.append(item)
                self.total_count += 1
        else:
            self.internal_storage.append(data)
            self.total_count += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                else:
                    pass
        elif isinstance(data, dict):
            return True
        else:
            return False
        return True

    def ingest(self, data: (dict[str, Any] | list[dict[str, Any]])) -> None:
        if self.validate(data) is False:
            print(f"Test invalid ingestion of string \
'{data}' without prior validation:")
            raise TypeError("Got exception: Improper log data")
        if isinstance(data, list):
            for item in data:
                stri = f"{item['log_level']}: {item['log_message']}"
                self.internal_storage.append(stri)
                self.total_count += 1
        else:
            stri = f"{data['log_level']}: {data['log_message']}"
            self.internal_storage.append(stri)
            self.total_count += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
    stream.register_processor(num)

    mixed_data = ['Hello world', [3.14, -1, 2.71], [{'log_leve\
l': 'WARNING', 'log_message': 'Telnet access\
!Use ssh instead'}, {'log_level': 'INFO', 'log_\
message': 'User wilis connected'}], 42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {mixed_data}")

    stream.process_stream(mixed_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(mixed_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nConsume some elements from the data \
processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num.output()
    for _ in range(2):
        text.output()
    log.output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
