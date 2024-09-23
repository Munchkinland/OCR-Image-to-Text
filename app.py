import os
import easyocr

def extract_text_from_image(image_path, reader):
    # Read text from image
    result = reader.readtext(image_path)
    
    # Extract text from result
    extracted_text = ' '.join([text[1] for text in result])
    
    return extracted_text

def process_images_in_directory(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['es', 'en'])  # For Spanish and English
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpeg', '.jpg', '.png', '.bmp', '.gif')):
            image_path = os.path.join(input_dir, filename)
            try:
                extracted_text = extract_text_from_image(image_path, reader)
                
                # Create output filename (replace image extension with .txt)
                output_filename = os.path.splitext(filename)[0] + '.txt'
                output_path = os.path.join(output_dir, output_filename)
                
                # Write extracted text to individual file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(extracted_text)
                
                print(f"Processed {filename}. Text saved to {output_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Usage
input_directory = 'images'
output_directory = 'extracted_texts'

process_images_in_directory(input_directory, output_directory)
print(f"Text extraction complete. Results saved to individual files in {output_directory}")

# Created/Modified files during execution:
print(f"Created files: {[f for f in os.listdir(output_directory) if f.endswith('.txt')]}")