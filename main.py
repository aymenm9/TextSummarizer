from app_argv import creat_argparse
from file_io import get_str_from_file, write_to_file
from choice_algo import get_algo
from max import summarize as max_summarize
import sys
def main():
    args_parser = creat_argparse()
    args = args_parser.parse_args()
    if not args.input:
        args_parser.print_help()
        sys.exit(1)
    input_file = args.input
    output_file = args.output if args.output else 'output.txt' 
    algorithm = args.algorithm if args.algorithm else 'TextRank'
    limit = args.limit if args.limit else 5
    language = args.language if args.language else 'english'
    sentence_limit = args.sentence_limit
    content = get_str_from_file(input_file)
    summarize = get_algo(algorithm)
    summary = summarize(content,limit=limit,text_language=language)
    if sentence_limit:
        summary = max_summarize(summary,summarize,limit=sentence_limit)
    write_to_file(file_name=output_file, content=summary)
    

if __name__ == '__main__':
    main()