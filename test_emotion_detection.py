from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result.get("dominant_emotion", 0), "joy")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result.get("dominant_emotion", 0), "anger")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result.get("dominant_emotion", 0), "disgust")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result.get("dominant_emotion", 0), "sadness")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result.get("dominant_emotion", 0), "fear")

unittest.main()