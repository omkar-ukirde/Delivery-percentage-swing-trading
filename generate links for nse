def generate_urls(formatted_date, formatted_today, symbols):
    base_url = "https://www.nseindia.com/api/historical/securityArchives"
    data_type = "priceVolumeDeliverable"
    series = "ALL"
    csv_format = "true"

    # Generate URLs for each symbol
    urls = [
        f"{base_url}?from={formatted_date}&to={formatted_today}&symbol={s}&dataType={data_type}&series={series}&csv={csv_format}"
        for s in symbols
    ]

    return urls

# Example usage:
formatted_date = "28-11-2023"
formatted_today = "29-12-2023"
symbols_list = [
    'BHARATWIRE', 'EXCELINDUS', 'SPECIALITY', 'ANUP', 'SKIPPER', 'AJMERA', 'SHALPAINTS', 'GMBREW', 'SANGAMIND', 'SHIVALIK',
    'GMRP&UI', 'PENIND', 'GEOJITFSL', 'BCLIND', 'DBOL', 'SHAILY', 'LIKHITHA', 'MADRASFERT', 'STEELCAS', 'MKPL', 'ROSSELLIND',
    'KITEX', 'PRAKASH', 'ARTEMISMED', 'RICOAUTO', 'OMAXE', 'CENTUM', 'ROTO', 'PRECAM', 'BIGBLOC', 'SHREDIGCEM', 'CLSEL',
    'GTLINFRA', 'PGIL', 'UTTAMSUGAR', 'AVADHSUGAR', 'PITTITIND', 'SPORTKING', 'DEEPINDS', 'PARAGMILK', 'AGARIND', 'CONTROLPR',
    'BAJAJHCARE', 'KAMDHENU', 'CHEMCON', 'GICHSGFIN', 'MEDICAMEQ', 'DLINKINDIA', 'ARIHANTSUP', 'VHL', 'PFS', 'HEXATRADEX',
    'RILINFRA', 'CAPACITE', 'SPAL', 'NCLIND', '63MOONS', 'NAVKARCORP', 'ORIENTPPR', 'DREDGECORP', 'AMBIKCO', 'CENTRUM',
    'LINC', 'RGL', 'SCHAND', 'NELCAST', 'FAZE3Q', 'KICL', 'DVL', 'JAGSNPHARM', 'POKARNA', 'IFGLEXPOR', 'TRIL', 'CENTENKA',
    'SMCGLOBAL', 'ROHLTD', 'INDNIPPON', 'SHAKTIPUMP', 'NGLFINE', 'IMPAL', 'BLISSGVS', 'ALLSEC', 'ORIENTBELL', 'MANGLMCEM',
    'SANDESH', 'BODALCHEM', 'ESTER', 'ZOTA', 'RSWM', 'INDRAMEDCO', 'QUICKHEAL', 'SRHHYPOLTD', 'AURIONPRO', 'GSLSU', 'SASTASUNDR',
    'MANAKSIA', 'AWHCL', 'BLKASHYAP', 'RAMRAT', 'JINDRILL', 'VIMTALABS', 'CLOUD', 'DPABHUSHAN', 'MOLDTECH', 'ATULAUTO',
    'KOKUYOCMLN', 'SIGACHI', 'HIMATSEIDE', 'LINCOLN', 'GREENPOWER', 'EMAMIPAP', 'SATINDLTD', 'RAMCOSYS', 'HPAL', 'OCCL',
    'FOCUS', 'GEPIL', 'SUTLEJTEX', 'PANACEABIO', 'JAIBALAJI', 'RML', 'JETAIRWAYS', 'TRACXN', 'KHAICHEM', 'TNPETRO', 'ONWARDTEC',
    'TFCILTD', 'ONMOBILE', 'INNOVANA', 'GANDHITUBE', 'TEXINFRA', 'MEDICO', 'TVSELECT', 'HEUBACHIND', 'VINYLINDIA', 'PARACABLES',
    'FOODSIN', 'HLVLTD', 'COFFEEDAY', 'BETA', 'APEX', 'YUKEN', 'ELIN', 'MONARCH', 'DMCC', 'CHEVIOT', 'XCHANGING', 'VISAKAIND',
    'SUMMITSEC', 'SUKHJITS', 'INDIANHUME', 'JUBLINDS', 'ASALCBR', 'DECCANCE', 'JAYBARMARU', 'COOLCAPS', 'APOLLO', 'ELDEHSG',
    'HERCULES', '4THDIM', 'KRITI', 'AGSTRA', 'NAHARPOLY', 'MANINDS', 'ENIL', 'SYNCOMF', 'KAMOPAINTS', 'NAGAFERT', 'SCPL', 'HPL',
    'INDOAMIN', 'DCMSRIND', 'MENONBE', 'VASCONEQ', 'VLSFINANCE', 'BALAXI', 'ZEEMEDIA', 'CREATIVE', 'KRISHIVAL', 'SNOWMAN', 'KOPRAN',
    'SHREYAS', 'REFEX', 'KSOLVES', 'GFLLIMITED']


urls = generate_urls(formatted_date, formatted_today, symbols)

# Display the generated URLs
for url in urls:
    print(url)
