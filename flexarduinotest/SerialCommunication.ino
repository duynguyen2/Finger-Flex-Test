class SerialCommunication : public ICommunication {
  private:
    bool cIsOpen;

  public:
    SerialCommunication() {
      cIsOpen = false;
    }

    bool isOpen() {
      return cIsOpen;
    }

    void start() {
      Serial.begin(SERIAL_BAUD_RATE);
      cIsOpen = true;
    }

    void output(char *data) {
      Serial.print(data);
      Serial.flush();
    }

    bool readData(char *input) {
      byte size = Serial.readBytesUntil('\n', input, 100);
      input[size] = NULL;
      return input != NULL && strlen(input) > 0;
    }
};
