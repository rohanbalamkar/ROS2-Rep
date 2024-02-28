from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rohan',
    maintainer_email='rohan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sim = my_pkg.simple:main',
            "my_pub = my_pkg.my_publisher:main",
            "my_sub = my_pkg.my_subscriber:main",
            'my_control = my_pkg.turtle_controller:main',
            'client = my_pkg.client:main',
            'server = my_pkg.server:main',
        ],
    },
)
