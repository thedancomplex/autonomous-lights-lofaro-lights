#!/bin/bash


tplight raw 10.66.2.21 '{"smartlife.iot.smartbulb.lightingservice":{"transition_light_state":{"ignore_default":1,"on_off":1,"color_temp":0,"hue":$1,"saturation":$2}}}'

