import argparse
import asyncio


def sizeof_fmt(num: int, suffix: str = 'B') -> str:
    """
    Return file size in human readable format.
    :param num:
    :param suffix:
    :return: The human readable string of file size
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

async def download_file(
        url: str,min_chunk_size: int,max_chunk_size: int,output: str
) -> bool:


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Downloader')
    parser.add_argument("url",metavar='URL', type=str, help='URL to download')
    parser.add_argument(
        "--min-chunk-size", type=int, help="minimum file chunk size (default: 10MB)"
    )
    parser.add_argument(
        "--max-chunk-size", type=int, help="maximum file chunk size (default: 100MB)"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="output file path (default: current working directory)",
    )
    args = parser.parse_args()
    if args.url:
        saved = asyncio.run(
            download_file(
                url=args.url,
                min_chunk_size=args.min_chunk_size,
                max_chunk_size=args.max_chunk_size,
                output=args.output
            )
        )
        if saved:
            print('File download completed! :)')
        else:
            print('File download Failed! :(')
