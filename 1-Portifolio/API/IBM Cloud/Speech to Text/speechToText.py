import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource

##########
# IBM CLOUD: Use the following code only to
# authenticate to IBM Cloud.
##########

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
try:
    authenticator = IAMAuthenticator('QGHYFQa6LWoLDCR-UMMT7W4DCW7zP3kuOih7YfXuLAOc')
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/b29192ff-d0c2-4bce-baca-66a7652d02ec/v1/recognize')



    # Invoke a method
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)



speech_to_text.set_default_headers({'x-watson-learning-opt-out': "true"})

dict recognize_using_websocket(
  audio=None, 
  content_type=None,
  recognize_callback=None, model=None,
  language_customization_id=None, acoustic_customization_id=None,
  customization_weight=None, base_model_version=None,
  inactivity_timeout=None, interim_results=None,
  keywords=None, keywords_threshold=None,
  max_alternatives=None, word_alternatives_threshold=None,
  word_confidence=None, timestamps=None, profanity_filter=None,
  smart_formatting=None, speaker_labels=None, http_proxy_host=None,
  http_proxy_port=None, customization_id=None, grammar_name=None,
  redaction=None, processing_metrics=None, processing_metrics_interval=None,
  audio_metrics=None, end_of_phrase_silence_time=None,
  split_transcript_at_phrase_end=None, speech_detector_sensitivity=None,
  background_audio_suppression=None, **kwargs)
##########
# IBM CLOUD PAK FOR DATA: Use the following code
# only to authenticate to IBM Cloud Pak for Data.
##########

# from ibm_cloud_sdk_core.authenticators import CloudPakForDataAuthenticator
# authenticator = CloudPakForDataAuthenticator(
#     '{username}',
#     '{password}',
#     'https://{cpd_cluster_host}{:port}'
# )
# speech_to_text = SpeechToTextV1(
#     authenticator=authenticator
# )
# speech_to_text.set_service_url('{url}')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()
print("before audioLane.mpeg")

with open(join(dirname(__file__), './.', 'audioLane.mpeg'),
              'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/mpeg',
        recognize_callback=myRecognizeCallback,
        model='pt-BR_BroadbandModel',
        keywords=['epilepsia', 'Elisangela', 'convulsao'],
        keywords_threshold=0.5,
        max_alternatives=3)

print("end?")

    
#from ibm_watson import SpeechToTextV1
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#authenticator = IAMAuthenticator('{QGHYFQa6LWoLDCR-UMMT7W4DCW7zP3kuOih7YfXuLAOc}')
#speech_to_text = SpeechToTextV1( 
#    authenticator=authenticator
#)

#speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com')


#dict recognize_using_websocket(audio, content_type,
#  recognize_callback, model=None,
#  language_customization_id=None, acoustic_customization_id=None,
#  customization_weight=None, base_model_version=None,
#  inactivity_timeout=None, interim_results=None,
#  keywords=None, keywords_threshold=None,
#  max_alternatives=None, word_alternatives_threshold=None,
#  word_confidence=None, timestamps=None, profanity_filter=None,
#  smart_formatting=None, speaker_labels=None, http_proxy_host=None,
#  http_proxy_port=None, customization_id=None, grammar_name=None,
#  redaction=None, processing_metrics=None, processing_metrics_interval=None,
#  audio_metrics=None, end_of_phrase_silence_time=None,
#  split_transcript_at_phrase_end=None, speech_detector_sensitivity=None,
#  background_audio_suppression=None, **kwargs)
