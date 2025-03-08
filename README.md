# tts
This Python script converts text files into audio files (.mp3) using Microsoft Edge's text-to-speech service. It efficiently processes multiple text files and generates audio files in a specified voice.

Key Features

Converts text files to audio files (.mp3)
Processes multiple files at once
Efficient audio generation with asynchronous processing
Voice customization (change voice type)
Usage

Convert a single file: python tts_generator.py filename.txt
Convert multiple files: python tts_generator.py *.txt
Change voice type: Modify the VOICE variable in the script
Output

Generated audio files are saved in the output directory.


このPythonスクリプトは、テキストファイルをMicrosoft Edgeのテキスト読み上げサービスを使用して音声ファイル（.mp3）に変換するツールです。複数のテキストファイルを効率的に処理し、指定された音声で音声ファイルを生成します。

主な機能

テキストファイルから音声ファイル（.mp3）への変換
複数のファイルを一度に処理可能
非同期処理による効率的な音声生成
音声のカスタマイズ（音声種類の変更）
使用方法

単一ファイルの変換: python tts_generator.py ファイル名.txt
複数ファイルの変換: python tts_generator.py *.txt
音声種類の変更: スクリプト内のVOICE変数を変更
出力

生成された音声ファイルはoutputディレクトリに保存されます。
