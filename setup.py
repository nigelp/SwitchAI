from setuptools import setup, find_packages


def deps_list(*pkgs):
    return [deps[pkg] for pkg in pkgs]


deps = ["pydantic"]

extras = {}

extras["openai"] = deps_list("openai")
extras["mistralai"] = deps_list("mistralai")
extras["anthropic"] = deps_list("anthropic")
extras["google-generativeai"] = deps_list("google-generativeai")
extras["deepgram-sdk"] = deps_list("deepgram-sdk")
extras["voyageai"] = deps_list("voyageai")

extras["all"] = (
    extras["openai"]
    + extras["mistralai"]
    + extras["anthropic"]
    + extras["google-generativeai"]
    + extras["deepgram-sdk"]
    + extras["voyageai"]
)

setup(
    name="switchai",
    version="0.2.4",
    description="A unified library for interacting with various AI APIs through a standardized interface.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Yassine El Boudouri",
    author_email="boudouriyassine@gmail.com",
    url="https://github.com/yelboudouri/SwitchAI",
    license="Apache 2.0 License",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=deps,
    extras_require=extras,
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
