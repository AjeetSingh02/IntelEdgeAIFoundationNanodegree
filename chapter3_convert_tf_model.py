# To convert the SSD MobileNet V2 model from TensorFlow

# Download and unzip the model
# cd into the model

# To shorten the path by creating ENV variable
! export MOD_OPT=/opt/intel/openvino/deployment_tools/model_optimizer

# Write in same line
! python $MOD_OPT/mo.py 
	--input_model frozen_inference_graph.pb 
	--tensorflow_object_detection_api_pipeline_config pipeline.config 
	--reverse_input_channels 
	--tensorflow_use_custom_operations_config $MOD_OPT/extensions/front/tf/ssd_v2_support.json
