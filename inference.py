from image_preprocessing import preprocess_image_for_inference
from transformers import pipeline

def predict(path_im, pipe):
  prediction = pipe(preprocess_image_for_inference(path_im))
  most_probable_prediction = prediction[0]['label']
  if most_probable_prediction != 'N':
    return "Abnormal ECG signal. " + most_probable_prediction + " case is suggested."
  else:
    return "Normal ECG signal. Score: " + str(prediction[0]['score'])
