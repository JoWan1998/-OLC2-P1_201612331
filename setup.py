from setuptools import setup

setup(
    name='AUGUS_OLC2_P1_201612331',
    version='1.0.0',
    packages=['ply', 'wdes'],
    url='https://github.com/ProyectosWannan',
    license='GNU GPL V.3',
    author='Jose Wannan',
    author_email='299399310101@ingenieria.usac.edu.gt',
    description='Proyecto 1, Compiladores 2, UNIVERSIDAD DE SAN CARLOS DE GUATEMALA',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.8.3',
    windows=[
        {
            "script": "Form.py",
            "icon_resources": [(1, "augus.ico")]}
    ]

)
