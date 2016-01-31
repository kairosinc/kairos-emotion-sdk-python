from KairosEmotionAPILib.Controllers.EmotionAnalysisController import *

controller = EmotionAnalysisController()
response = controller.create_media('http://media.kairos.com/test.flv')
