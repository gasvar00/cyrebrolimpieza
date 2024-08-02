import shutil
import os
import subprocess

# Set the source and destination directories
src = '/store/persistent_queue/dlc.dlc'
dst = '/home/backup'

# Create the destination directory if it does not exist
if not os.path.exists(dst):
  os.makedirs(dst)

# Iterate through the files in the source directory
for file in os.listdir(src):
  # Construct the full path to the file
  src_path = os.path.join(src, file)
  dst_path = os.path.join(dst, file)

  # Check if the file is a regular file (not a directory)
  if os.path.isfile(src_path):
    # Move the file from the source to the destination
    shutil.move(src_path, dst_path)

# Run the command to restart the dlc service
subprocess.run(['systemctl', 'restart', 'dlc'])

print('Queue cleared, restart: Done')
