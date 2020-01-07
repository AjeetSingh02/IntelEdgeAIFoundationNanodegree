# Downloading Models


# To navigate to the directory containing the Model Downloader:
! cd /opt/intel/openvino/deployment_tools/open_model_zoo/tools/downloader

# Downloading Human Pose Model
! sudo ./downloader.py --name human-pose-estimation-0001 -o /home/workspace

# Downloading Text Detection Model
! sudo ./downloader.py --name text-detection-0004 --precisions FP16 -o /home/workspace

# Downloading Car Metadata Model
! sudo ./downloader.py --name vehicle-attributes-recognition-barrier-0039 --precisions INT8 -o /home/workspace