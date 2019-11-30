PYRCC := pyrcc5
PYUIC := /home/kli/anaconda3/bin/pyuic5

PATH := windows

UIFILES := $(wildcard $(PATH)/*.ui)
PYUIFILES := $(UIFILES:.ui=.py)
$(info Compiling files: $(UIFILES))

RESFILES := $(wildcard *.qrc)
PYRESFILES := $(RESFILES:.qrc=_rc.py)

.PHONY: all
all: $(PYUIFILES) $(PYRESFILES)

%.py: %.ui
	$(PYUIC) $< -o $@

%_rc.py: %.qrc
	$(PYRCC) $< -o $@

# clean :
# 	$(RM) $(COMPILED_UI) $(COMPILED_RESOURCES) $(COMPILED_UI:.py=.pyc) $(COMPILED_RESOURCES:.py=.pyc)
