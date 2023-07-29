include ../build_tools/poetry.mk
POETRY_VERSION=1.5.1

# Vault will inject the secrets of the project 
# that is currently configured as environemnt variables
# `vlt config`
# `vlt secrets`
run:
	vlt run -c 'python core/main.py'
