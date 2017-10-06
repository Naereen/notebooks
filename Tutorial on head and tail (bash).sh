
export LANGUAGE=en  # Be sure the commands output English text

head --help

cat /etc/dictionaries-common/words > /tmp/file.txt

head /tmp/file.txt

head -n 20 /tmp/file.txt

wc -l /tmp/file.txt

head -n 100 /tmp/file.txt | wc -l  # 100 lines, from 1st to 100th
head -n -100 /tmp/file.txt | wc -l  # All lines but the last 100 lines, from 1st to 99071th

tail --help

tail /tmp/file.txt  # Last 10 lines

tail -n 20 /tmp/file.txt  # Last 20 lines

tail -n 100 /tmp/file.txt | wc -l  # 100 lines, from 99071th to 99171th
tail -n +101 /tmp/file.txt | wc -l  # All lines from line 101, from 101th to 99171th
