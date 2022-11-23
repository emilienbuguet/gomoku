NAME	:= pbrain-gomoku-ai

MAIN	:= sources/main.py

ifeq ($(OS), Windows_NT)
	NAME = .exe
else
	NAME = pbrain-gomoku-ai
endif

all: $(NAME)

ifeq ($(OS), Windows_NT)
$(NAME):
	@pyinstaller $(MAIN) --onefile --name $(NAME)
	@cp ./dist/$(NAME) .
else
$(NAME):
	@cp ./sources/unix_main.py ./$(NAME)
	@chmod +x ./$(NAME)
endif


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
