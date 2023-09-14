from bing_image_downloader import downloader

# IMAGE DOWNLOAD
downloader.download('Cucumber', limit=300, output_dir='',
                    adult_filter_off=True, force_replace=False,
                    timeout=60)
downloader.download('Tomato', limit=300, output_dir='',
                    adult_filter_off=True, force_replace=False,
                    timeout=60)


