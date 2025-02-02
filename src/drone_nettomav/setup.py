from setuptools import setup

package_name = 'drone_nettomav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='afrobudha',
    maintainer_email='afrobudha@todo.todo',
    description='Sending info from neural net to mavlink',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'commander = drone_nettomav.commander:main',
            'receiver = drone_nettomav.receiver:main',
        ],
    },
)
