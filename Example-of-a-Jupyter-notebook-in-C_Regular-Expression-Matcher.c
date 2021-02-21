#include <stdio.h>

int match(char *regexp, char *text);
int matchhere(char *regexp, char *text);
int matchstar(int c, char *regexp, char *text);

/* match: search for regexp anywhere in text */
int match(char *regexp, char *text)
{
    if (regexp[0] == '^')
        return matchhere(regexp+1, text);
    do {    /* must look even if string is empty */
        if (matchhere(regexp, text))
            return 1;
    } while (*text++ != '\0');
    return 0;
}

/* matchhere: search for regexp at beginning of text */
int matchhere(char *regexp, char *text)
{
    if (regexp[0] == '\0')
        return 1;
    if (regexp[1] == '*')
        return matchstar(regexp[0], regexp+2, text);
    if (regexp[0] == '$' && regexp[1] == '\0')
        return *text == '\0';
    if (*text!='\0' && (regexp[0]=='.' || regexp[0]==*text))
        return matchhere(regexp+1, text+1);
    return 0;
}

/* matchstar: search for c*regexp at beginning of text */
int matchstar(int c, char *regexp, char *text)
{
    do {    /* a * matches zero or more instances */
        if (matchhere(regexp, text))
            return 1;
    } while (*text != '\0' && (*text++ == c || c == '.'));
    return 0;
}

int main(int argc, char *argv) {
    char* regexp = "ab.*d.*f";
    printf("For regexp %s\n", regexp);
    
    char* text1   = "abccdeff";  // okay
    printf("For text %s,", text1);
    printf(" result = %d\n", match(regexp, text1));
    
    char* text2   = "abcokokazodkaozkdazkdcdeff";  // okay
    printf("For text %s,", text2);
    printf(" result = %d\n", match(regexp, text2));
    
    char* text3   = "abdf";  // okay
    printf("For text %s,", text3);
    printf(" result = %d\n", match(regexp, text3));
    
    char* text4   = "abdddffff";  // okay
    printf("For text %s,", text4);
    printf(" result = %d\n", match(regexp, text4));
    
    char* text5   = "SSZSabdddffffZDZD";  // okay
    printf("For text %s,", text5);
    printf(" result = %d\n", match(regexp, text5));
    
    
    char* text11   = "Abccdeff";  // pas okay
    printf("For text %s,", text11);
    printf(" result = %d\n", match(regexp, text11));
    
    char* text12   = "aZcokokazodkaozkdazkdcdeff";  // pas okay
    printf("For text %s,", text12);
    printf(" result = %d\n", match(regexp, text12));
    
    char* text13   = "abZZf";  // pas okay
    printf("For text %s,", text13);
    printf(" result = %d\n", match(regexp, text13));
    
    char* text14   = "XXaZDbZDdZDdZDdZDfZDfZDfZDfXX";  // pas okay
    printf("For text %s,", text14);
    printf(" result = %d\n", match(regexp, text14));

    return 0;
}

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <stdio.h>
#include <unistd.h>
#include <stdarg.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>

#define GREEDY_BRANCH 1
#define LAZY_BRANCH 0

int split(int branch1, int branch2){
  /*  This function is just a fancy way to do a 'fork' call that will split this
      process and execute 'branch1', then 'branch2' of the outer 'if' statement
      where this function is called.  It will also wait sequentially for 'branch1'
      to finish before running 'branch2' rather than running both in parallel.
      If 'branch1' returns 0 to indicate success, then 'branch2' will never run. */
  pid_t child_pid;
  pid_t wpid;
  int status = 0;

  if((child_pid = fork()) > 0)
    while ((wpid = wait(&status)) > 0);/*  Wait on child to finish in 'branch1'.  */
  else
    return branch1;/*  If this is child, return and contine in 'branch1'. */

  if(WIFEXITED(status)){
    if(WEXITSTATUS(status) == 0) /* Match found in 'branch1', exit the parent with 0. */
      exit(0);
    else
      /*  Continue on to check second branch... */;
  }else{
    printf("Unexpected Error Case.\n");
    exit(1);
  }

  if((child_pid = fork()) > 0)
    while ((wpid = wait(&status)) > 0);/*  Wait on child to finish in 'branch2'.  */
  else
    return branch2;/*  If this is child, return and contine in 'branch2'. */

  if(WIFEXITED(status)){
    if(WEXITSTATUS(status) == 0) /* Match found in 'branch2', exit the parent with 0. */
      exit(0);
    else
      exit(1); /*  Neither branch found a match. */
  }else{
    printf("Unexpected Error Case.\n");
    exit(1);
  }
}

int matches_one_of_these_characters(char c, int num_chars, ...){
  va_list arglist;
  va_start(arglist, num_chars);
  int i;
  int found = 0;
  for(i = 0; i < num_chars; i++){
    int d = (char)va_arg(arglist, int);
    if(c == d){
      found = 1;
    }
  }
  va_end(arglist);
  return found;
}

int matches_this_character(char available, char required){
  if(available == required){
    return 1;
  }else{
    return 0;
  }
}

char safely_get_character(const char * str, int offset, int pos, int str_len){
  if(offset + pos < str_len){
    return str[offset + pos];
  }else{
    exit(1); /*  End of string reached.*/
  }
}

int is_beginning_of_text(int position_in_string){
  return position_in_string == 0;
}

int is_end_of_text(int position_in_string, int str_len){
  return str_len == position_in_string;
}

/*  The following C program is a hard-coded implementation of
    the regular expression 'ab.*d.*f'.  */
int regex_search_at_offset(const char * str, int str_len, int offset){
  int status = 0;
  if(fork() > 0){  /*  If this is the parent */
    while (wait(&status) > 0); /*  Wait on child to finish. */
    if(WIFEXITED(status)){  /*  Then, return the return code of the child. */
      return WEXITSTATUS(status);
    }else{
      printf("Unexpected Error Case.\n");
      exit(1);
    }
  }else{/* Continue with the search in a child process and send exit code to parent. */
    int pos = 0; /*  The position we're currently checking in the search string. */
    char current_character;
    /*  Begin our regex search. */
    current_character = safely_get_character(str, offset, pos, str_len);
    if(matches_this_character(current_character, 'a')){
      pos++;
    }else{
      exit(1);
    }
    current_character = safely_get_character(str, offset, pos, str_len);
    if(matches_this_character(current_character, 'b')){
      pos++;
    }else{
      exit(1);
    }
    node_8:
    if(split(GREEDY_BRANCH, LAZY_BRANCH) > 0){
      current_character = safely_get_character(str, offset, pos, str_len);
      if(!matches_one_of_these_characters(current_character, 2, '\n', '\r')){
        pos++;
      }else{
        exit(1);
      }
      goto node_8;
    }else{
      current_character = safely_get_character(str, offset, pos, str_len);
      if(matches_this_character(current_character, 'd')){
        pos++;
      }else{
        exit(1);
      }
      node_5:
      if(split(GREEDY_BRANCH, LAZY_BRANCH) > 0){
        current_character = safely_get_character(str, offset, pos, str_len);
        if(!matches_one_of_these_characters(current_character, 2, '\n', '\r')){
          pos++;
        }else{
          exit(1);
        }
        goto node_5;
      }else{
        current_character = safely_get_character(str, offset, pos, str_len);
        if(matches_this_character(current_character, 'f')){
          pos++;
        }else{
          exit(1);
        }
        /*  We've got a match. */
        printf("Found this match of length %d starting at offset %d:\n", pos, offset);
        for(int i = 0; i < pos; i++){
          printf("%c", str[offset + i]);
        }
        printf("\n");
        exit(0);
      }
    }
  }
}

int main(int argc, char *argv[]){
  // For text "abccdeff", result = 1
  // For text "abcokokazodkaozkdazkdcdeff", result = 1
  // For text "abdf", result = 1
  // For text "abdddffff", result = 1
  // For text "SSZSabdddffffZDZD", result = 1
  // For text "Abccdeff", result = 0
  // For text "aZcokokazodkaozkdazkdcdeff", result = 0
  // For text "abZZf", result = 0
  // For text "XXaZDbZDdZDdZDdZDfZDfZDfZDfXX", result = 0

  /* The string to search. You can change this to anything. */
  const char * str = "abcokokazodkaozkdazkdcdeff";
  int str_len = (int)strlen(str);
  printf("Let's try to match the string '%s' with the regex 'ab.*d.*f'\n", str);
  for(int offset = 0; offset < str_len; offset++){
    if(regex_search_at_offset(str, str_len, offset) == 0){
      exit(0);
    }
  }
  printf("No match Found!\n");
  return 1;
}
