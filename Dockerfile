FROM python:3.8
ARG VERSION
LABEL org.label-schema.version=$VERSION
COPY ./requirements.txt /webapp/requirements.txt
WORKDIR /webapp
RUN pip install -r requirements.txt
COPY ./webapp/app.py /webapp/app.py
COPY ./webapp/model.h5 /webapp/model.h5
COPY webapp/templates/* /webapp/templates/
COPY webapp/uploads/* /webapp/uploads/
EXPOSE 5000 5050
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]