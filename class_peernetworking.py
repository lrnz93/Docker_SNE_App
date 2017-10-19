from flask import Flask, session
from flask.views import MethodView
from class_runningconfig import RunningConfig


class DistAPIReset(MethodView):
    def post(self):
        ip = RunningConfig().get_config('ip')
        port = RunningConfig().get_config('port')
        return 'DO POST DistAPIReset ACTION for ' + ip + ':' + port

    def _exectute_reset(self):
        # TODO Do reset call
        return None


class DistAPIDocInfo(MethodView):
    def post(self):
        return 'DO POST DistAPIDocInfo ACTION'
