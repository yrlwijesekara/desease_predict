import tensorflow as tf
import json

# Load the model
model = tf.keras.models.load_model('final_enhanced_plant_disease_model.h5')

# The actual class names from the training (from the notebook output)
class_names = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

print(f"Model expects {model.output_shape[-1]} classes")
print(f"We have {len(class_names)} class names")
print("\nClass names:")
for i, name in enumerate(class_names):
    print(f"{i}: {name}")

# Save to JSON
with open('class_names.json', 'w') as f:
    json.dump(class_names, f, indent=2)

print("\n✅ Class names saved to class_names.json")
