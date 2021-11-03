# automating the deletion and creation of new bots

# clear all the previous agent files
rm -rf .bin bot/__pycache__ __pycache__ lib/__pycache__ 

# create new guy
python builder.py -i 127.0.0.1 -p 8080 -n testagent

# let the silly dev know what's going on
echo "-------------------------------------------------------------"
echo "---- Built 'testagent' targetting port 8080 on 127.0.0.1 ----"
echo "-------------------------------------------------------------"
echo "\n\n"

# Now make running everything easy
echo "Now run the agent:"
echo "./testagent_  -- or -- open testagent_.exe"
