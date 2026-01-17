'''
read -p "Please enter your name " NAME
echo "Welcome " $NAME
read -ep "What is your name? " FIRST_NAME LAST_NAME

read -sep "What is you password" PASSWORD
echo First Name: $FIRST_NAME, Last Name: $LAST_NAME, $PASSWORD

read -ep "Enter two intigers " x y

if [ $x -gt $y ] 
    then
    echo X: $x is greater than Y:$y
elif [ $x -eq $y ] 
    then
    echo X: $x is equal to Y: $y
else
    echo X: $x is less than Y: $y
fi
'''
for i in {1..5};
    do echo $i;
done
i=5
while [ $i -gt 0 ];do
    echo $i
    ((i--))
done