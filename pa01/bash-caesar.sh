#!/usr/bin/env bash

#message='YxB5TZx2BxAWTf BC2x1T!3TBCxyy6 4T560WWWTDB2TYADCDBT3!Az2U'
#read message
message="$(cat)"
message_len=${#message}

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
SYMBOLS_len=${#SYMBOLS}
#echo $SYMBOLS_len
#keeps track of best key
score=0
bestKey=0
#main
#-----------------------------------------
for (( key=0; key<$SYMBOLS_len; key++ ))
do
    translated=''

    for (( symbol=0; symbol<$message_len; symbol++ ))
    do
      #check if character from input text is in symbol set
      if [[ $SYMBOLS =~ "${message:$symbol:1}" ]]
      then
        for (( i=0; i<$SYMBOLS_len; i++ ))
        do
          if [[ "${SYMBOLS:$i:1}" == "${message:$symbol:1}" ]]
          then
            #echo "symbol =" ${SYMBOLS:$i:1}
            #echo "message = " ${message:$symbol:1} 
            symbolIndex=$i
          fi
        done
        #echo "symbol index" $symbolIndex
        translatedIndex=$(($symbolIndex-$key))
        if [[ $translatedIndex -lt 0 ]]
        then
          #echo $translatedIndex
          translatedIndex=$(($translatedIndex+$SYMBOLS_len))
        fi
        
        translated="${translated}${SYMBOLS:$translatedIndex:1}"
        #echo $translated
    
      else
        #echo "freak"
        translated="${translated}${message:$symbol:1}"
        #echo $tranlated
      fi
    done
    counter=0 
    for word in $translated
    do
        if grep -q -i $word "dictionary.txt"
        then
          ((counter++))
          #echo $word
        fi
    done
    #echo $key $counter
    #store key and score

    if [[ $counter -gt $score ]]
    then
        bestTrans=''
        bestTrans=$translated
        #redirect to output
        #echo $translated
        bestKey=$key
        score=$counter
    fi
    #echo $tranlated
    
    #echo $translated
done
#-----------------------------------------

#echo $bestKey
echo $bestTrans