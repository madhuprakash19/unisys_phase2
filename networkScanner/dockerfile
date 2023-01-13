FROM  python:3.10
RUN pip install numpy
RUN pip install pandas
RUN pip install pickle5
RUN pip install sklearn
RUN pip install scikit-learn
RUN pip install secure-smtplib
RUN pip install pyzmail36
RUN pip install imapclient
ADD dataSet.csv .
ADD train.py .
CMD [ "python","./train.py"]
