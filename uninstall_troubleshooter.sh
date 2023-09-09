#!/bin/bash

# Get the directory where the script is being executed
TROUBLESHOOTER_DIR=$PWD

# Remove the lines added to .bashrc from the bashrc.replace file
grep -v -f "$TROUBLESHOOTER_DIR/.bashrc.replace" ~/.bashrc > ~/.bashrc.tmp
mv ~/.bashrc.tmp ~/.bashrc

# Option to uninstall dependencies
read -p "Do you want to uninstall the dependencies installed for the troubleshooter? [y/N] " RESPONSE
if [[ $RESPONSE =~ ^([yY][eE][sS]|[yY])$ ]]
then
    pip uninstall -y -r "$TROUBLESHOOTER_DIR/requirements.txt"
fi

echo "Uninstallation complete. You may need to restart your terminal for all changes to take effect."
