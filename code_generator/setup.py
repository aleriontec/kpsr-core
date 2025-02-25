#****************************************************************************
#
#                           Klepsydra Core Modules
#              Copyright (C) 2019-2020  Klepsydra Technologies GmbH
#                            All Rights Reserved.
#
#  This file is subject to the terms and conditions defined in
#  file 'LICENSE.md', which is part of this source code package.
#
#  NOTICE:  All information contained herein is, and remains the property of Klepsydra
#  Technologies GmbH and its suppliers, if any. The intellectual and technical concepts
#  contained herein are proprietary to Klepsydra Technologies GmbH and its suppliers and
#  may be covered by Swiss and Foreign Patents, patents in process, and are protected by
#  trade secret or copyright law. Dissemination of this information or reproduction of
#  this material is strictly forbidden unless prior written permission is obtained from
#  Klepsydra Technologies GmbH.
#
#****************************************************************************

from setuptools import find_packages, setup

setup(
    name='kpsr_codegen',
    version='1.0',
    packages=find_packages(),
    package_data={
        'kpsr_codegen': ['conf/*.yaml', 'templates/*.*'],
    },
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'setuptools==58.5.3',
        'nose',
        'coverage',
        'lcov_cobertura',
        'Jinja2',
        'PyYaml'
    ],
    entry_points='''
        [console_scripts]
        kpsr_codegen = kpsr_codegen.__main__:main
    ''',
)
