def preprocessing(input_image, height, width):
    '''
    Given an input image, height and width:
    - Resize to height and width
    - Transpose the final "channel" dimension to be first
    - Reshape the image to add a "batch" of 1 at the start 
    '''
    image = cv2.resize(input_image, (width, height))
    image = image.transpose((2,0,1))
    image = image.reshape(1, 3, height, width)

    return image
	
#Human Pose
preprocessed_image = preprocessing(preprocessed_image, 256, 456)

#Text Detection
preprocessed_image = preprocessing(preprocessed_image, 768, 1280)

#Car Meta
preprocessed_image = preprocessing(preprocessed_image, 72, 72)


#To test your implementation, you can just run python test.py
