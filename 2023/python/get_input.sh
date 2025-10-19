# Check if an argument is provided, otherwise set a default value
chmod 777 get_input.sh
if [ -z "$1" ]; then
    day="0" # Set your default value here
else
    day="$1"
fi

if [ -z "$2" ]; then
    year="0" # Set your default value here
else
    year="$2"
fi

if [ -z "$3" ]; then
    input_file="in.txt" # Set your default value here
else
    input_file=$3
fi

echo $input_file

chmod 777 $input_file
python3 python_scripts/get_input.py "$day" "$year" > $input_file
chmod 400 $input_file

# Display a separator
echo "============================================================================================="

# Remove trailing newline characters from the end of the file
# tr -s '\n' < in.txt > temp.txt && mv temp.txt in.txt

# Display the first 5 lines of the file
echo "First 5 lines:"
head -n 5 $input_file

# Display a separator
echo "-----------------------"

# Display the last 2 lines of the file
echo "Last 2 lines:"
tail -n 2 $input_file

echo "============================================================================================="
echo ""
chmod 400 get_input.sh
