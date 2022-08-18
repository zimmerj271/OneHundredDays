import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """Basic representation of a video exporting codec"""

    @abstractmethod
    def prepare_export(selfself, video_data):
        """Prepares video data for exporting"""

    @abstractmethod
    def do_export(self, folder:pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec"""

    def prepare_export(selfself, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder:pathlib.Path):
        print(f"Exporting video data in losless format to {folder}")

class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile"""

    def prepare_export(selfself, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder:pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")

class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi244P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(selfself, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder:pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec"""

    @abstractmethod
    def prepare_export(clsself, audo_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder"""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(clsself, audo_data):
        print("Preparing audio data for AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec"""

    def prepare_export(clsself, audo_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}")


class ExporterFactory(ABC):
    """Factory that represents a combination of video and audio codecs.
    The factory is not the owner of the exporter objects: it does not maintain any
    of the instances. The factory simply creates the objects."""

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance"""

# Concrete factories are child classes of abstract class ExporterFactory
class LowQualityExporter(ExporterFactory):
    """Factory to provide a high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory to provide a slower speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory to provide a low speed, master quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()

# The main function has too many responsibilities.  It is handling all the operation of calling the different
# classes required to handle the audio and video operations: it asks the user for input, its responsible for mapping the
# objects to the desired functionality, and it handles the preparation and export methods
def main() -> None:
    """Main function"""

    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unknown output quality option: {export_quality}.")

    # Create the video and audio exporters
    # The object mapping using if/elif/else statement below causes the main function to need to
    # know a lot of information about the classes that it's calling in to perform the video and audio operations.
    # As a result, main has HIGH COUPLING.
    # This approach also makes it difficult to create new or custom formats.  Doing so results in more elif
    # conditions for additional object mapping.
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        # default master quality
        video_exporter = LosslessVideoExporter()
        audio_exporter = WAVAudioExporter()

    # prepare the export
    video_exporter.prepare_export("placeholder for video data")
    audio_exporter.prepare_export("placeholder for audio data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

# This function will handle the factory objects and will be
# the only place where we define the factories that are available
def read_exporter() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference."""
    factories = {
        "low": LowQualityExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }
    # read the desired export quality
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")


def main_with_factory(factory: ExporterFactory) -> None:
    """Main function using the Factory design pattern."""
    # The main function will be where the only place where a factory object is created
    # Now the main function is only responsible for retrieving the exporters, prepare, and export.

    # Instead of making main be responsible for calling in read_exporter and defining the factory exporter within the
    # main function, pass the selection of the exporter as a parameter of the main function.
    # factory = read_exporter()

    # Retrieve the video and audio exporters from the factory object
    video_exporter = factory.get_video_exporter()
    audio_exporter = factory.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder for video data")
    audio_exporter.prepare_export("placeholder for audio data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    # main_with_factory()
    main_with_factory(HighQualityExporter())  # This is an example of dependency injection