
using System;
using System.IO;
using System.Linq;
using MediaToolkit;
using MediaToolkit.Model;

class Program
{
    static void Main(string[] args)
    {
        // Get the current directory and specify the temp folder
        string currentDirectory = AppDomain.CurrentDomain.BaseDirectory;
        string tempDirectory = Path.Combine(currentDirectory, "temp");

        // Check if the temp directory exists
        if (!Directory.Exists(tempDirectory))
        {
            Console.WriteLine("The 'temp' directory does not exist.");
            return;
        }

        // Find video and audio files in the temp directory
        var videoFiles = Directory.GetFiles(tempDirectory)
                                  .Where(file => Path.GetFileName(file).Contains("temp_video"));
        var audioFiles = Directory.GetFiles(tempDirectory)
                                  .Where(file => Path.GetFileName(file).Contains("temp_audio"));

        if (!videoFiles.Any() || !audioFiles.Any())
        {
            Console.WriteLine("No matching video or audio files found.");
            return;
        }

        // Combine files
        foreach (var videoFile in videoFiles)
        {
            foreach (var audioFile in audioFiles)
            {
                string outputFileName = Path.Combine(tempDirectory, $"combined_{Path.GetFileName(videoFile)}");

                CombineAudioAndVideo(videoFile, audioFile, outputFileName);
            }
        }
    }

    static void CombineAudioAndVideo(string videoFilePath, string audioFilePath, string outputFilePath)
    {
        var inputFile = new MediaFile { Filename = videoFilePath };
        var audioFile = new MediaFile { Filename = audioFilePath };
        var outputFile = new MediaFile { Filename = outputFilePath };

        using (var engine = new Engine())
        {
            // Start the conversion
            engine.Convert(inputFile, outputFile, audioFile);
        }

        Console.WriteLine($"Combined {Path.GetFileName(videoFilePath)} and {Path.GetFileName(audioFilePath)} into {Path.GetFileName(outputFilePath)}.");
    }
}
