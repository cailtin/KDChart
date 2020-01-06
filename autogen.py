#!/usr/bin/env python
from autogen.autogen import autogen

project = "KDChart"
version = "2.99.50"
subprojects = ["KDChart", "KDGantt"]
prefixed = True

autogen(project, version, subprojects, prefixed, policyVersion = 2)
