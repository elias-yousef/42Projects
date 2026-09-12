from abc import ABC, abstractmethod
from typing import Any
import typing


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        self.CSVPlugin_list = []
        for items in data:
            self.CSVPlugin_list.append(items[1])
        last_string = ",".join(self.CSVPlugin_list)
        print(last_string)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        self.formatted_items = []
        total = 3
        for items in data:
            if len(items[1]) > 0:
                self.formatted_items.append(f'"item_{items[0]}": "{items[1]}"')
                total += 1
        last_string = ", ".join(self.formatted_items)
        print(f"{{{last_string}}}")


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
        try:
            current_storage = self.internal_storage.pop(0)
            self.rank_counter += 1
        except IndexError:
            current_storage = ""
        return (self.rank_counter - 1, current_storage)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for item in self.processors:
            i = 0
            self.temp_list = []
            while i < nb:
                self.temp_list.append(item.output())
                i += 1
            plugin.process_output(self.temp_list)

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
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(log)

    mixed_data = ['Hello world', [3.14, -1, 2.71], [{'log_leve\
l': 'WARNING', 'log_message': 'Telnet access \
!Use ssh instead'}, {'log_level': 'INFO', 'log_\
message': 'User wilis connected'}], 42, ['Hi', 'five']]

    print(f"Send first batch of data on stream: {mixed_data}")

    stream.process_stream(mixed_data)
    print("\n== DataStream statistics ==")

    CSV = CSVPlugin()
    stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSV)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    batch_two = [21, ['I love AI', 'LLMs are wonder\
ful', 'Stay healthy'], [{'log_level': 'ERROR\
', 'log_message': '500 server \
crash'}, {'log_level': 'NOTICE', 'log_message': 'Certificate \
expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {batch_two}")
    stream.process_stream(batch_two)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    JSON = JSONPlugin()
    stream.output_pipeline(5, JSON)
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
