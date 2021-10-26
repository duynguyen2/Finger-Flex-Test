classdef MQTTWrapperSubscribe

    properties
        returnMessage
        returnTopic
    end

    methods
        function obj = MQTTWrapperSubscribe(topic, address, clientID, port, QOS)
            persistent myMQTT;
            if isempty(myMQTT)
                myMQTT = mqtt('tcp://' + address, 'ClientID', clientID, 'Port', port);
            end

            persistent mySub
            if isempty(mySub)
                mySub = subscribe(myMQTT, topic, 'QOS', QOS);
                mySub.Callback = @myMQTT_Callback;
            end

            % callback function
            function myMQTT_Callback(topic, msg)
                fprint('MQTT callback topic "%s" : "%s"\n', topic, msg);
                obj.returnMessage = msg;
                obj.returnTopic = topic;
            end
        end
    end
end