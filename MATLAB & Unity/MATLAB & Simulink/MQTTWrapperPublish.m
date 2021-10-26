function MQTTWrapperPublish(input, topic, address, clientID, port, QOS)

persistent myMQTT;

if isempty(myMQTT)
    myMQTT = mqtt('tcp://' + address, 'ClientID' clientID, 'Port', port);
end

input_json = jsondecode(input);
publish(myMQTT, topic, input_json, 'QOS', QOS);
end