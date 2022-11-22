NAME	:= pbrain-gomoku-ai

MAIN	:= sources/main.py

ifeq ($(OS), Windows_NT)
	NAME = .exe
else
	NAME = pbrain-gomoku-ai
endif

all: $(NAME)

$(NAME):
	@pyinstaller $(MAIN) --onefile --name $(NAME)
	@cp ./dist/$(NAME) .

clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf __pycache__/
	@rm -f *.spec

fclean:	clean
	@rm -f $(NAME)

re:	fclean all

.PHONY:	all \
		clean \
		fclean \
		re
