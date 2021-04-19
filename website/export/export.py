def exportJSON_LD(phones):
    # file = open("website/static/export/phones.json")
    file = open("phones.jsonld", mode='w')
    for phone in phones:
        print("<script type=\"application/ld+json\">", file=file)
        print("{", file=file)
        print("\t\"@context\": \"https://schema.org\",", file=file)

        print("\t\"@type\": \"Product\",", file=file)

        print("\t\"category\": \"MobilePhone\",", file=file)

        print("\t\"name\": \"%s\"," % (phone[1]), file=file)

        print("\t\"offers\": {", file=file)
        print("\t\t\"@type\": \"Offer\",", file=file)
        print("\t\t\"price\": \"%.2f\"," % (phone[2]), file=file)
        print("\t\t\"priceCurrency\": \"CNY\"", file=file)
        print("\t},", file=file)

        print("\t\"size\": \"%.2f inch\"," % (phone[4]), file=file)

        print("\t\"image\": \"%s\"," % (phone[14]), file=file)

        print("\t\"brand\": {", file=file)
        print("\t\t\"@type\": \"Brand\",", file=file)
        print("\t\t\"name\": \"%s\"" % (phone[15]), file=file)
        print("\t},", file=file)

        print("\t\"additionalProperty\": [", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"System Kernel\",", file=file)
        print("\t\t\t\"value\": \"%s\"" % (phone[3]), file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Operating System\",", file=file)
        print("\t\t\t\"value\": \"%s\"" % (phone[5]), file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Resolution\",", file=file)
        print("\t\t\t\"value\": \"%s\"" % (phone[6]), file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Processor frequency\",", file=file)
        print("\t\t\t\"value\": \"%.2f\"," % (phone[7]), file=file)
        print("\t\t\t\"unitCode\": \"Ghz\"", file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Kernel number\",", file=file)
        print("\t\t\t\"value\": \"%d\"" % (phone[8]), file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"RAM capacity\",", file=file)
        print("\t\t\t\"value\": \"%d\"," % (phone[9]), file=file)
        print("\t\t\t\"unitCode\": \"GB\"", file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"ROM capacity\",", file=file)
        print("\t\t\t\"value\": \"%d\"," % (phone[10]), file=file)
        print("\t\t\t\"unitCode\": \"GB\"", file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Battery capacity\",", file=file)
        print("\t\t\t\"value\": \"%d\"," % (phone[11]), file=file)
        print("\t\t\t\"unitCode\": \"mAh\"", file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Rear camera pixels\",", file=file)
        print("\t\t\t\"value\": \"%d\"," % (phone[12]), file=file)
        print("\t\t\t\"unitCode\": \"megapixel\"", file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Front camera pixels\",", file=file)
        print("\t\t\t\"value\": \"%d\"," % (phone[13]), file=file)
        print("\t\t\t\"unitCode\": \"megapixel\"", file=file)
        print("\t\t},", file=file)
        print("\t\t{", file=file)
        print("\t\t\t\"@type\": \"PropertyValue\",", file=file)
        print("\t\t\t\"name\": \"Usage\",", file=file)
        print("\t\t\t\"value\": \"%s\"" % (phone[16]), file=file)
        print("\t\t}", file=file)
        print("\t]", file=file)
        print("}", file=file)
        print("</script>", file=file)
    file.close()


def exportXML(phones):
    # file = open("website/static/export/phones.xml")
    file = open("phones.xml", mode='w')
    for phone in phones:
        print("<div itemscope itemtype=\"https://schema.org/Product\">", file=file)
        print("\t<span itemprop=\"category\">mobilePhone</span>", file=file)
        print("\t<span itemprop=\"name\">%s</span>" % (phone[1]), file=file)
        print("\t<div itemprop=\"offers\" itemscope itemtype=\"https://schema.org/Offer\">", file=file)
        print("\t\t<span itemprop=\"price\">%.2f</span>" % (phone[2]), file=file)
        print("\t\t<span itemprop=\"priceCurrency\">CNY</span>", file=file)
        print("\t</div>", file=file)
        print("\t<span itemprop=\"size\">%.2f inch</span>" % (phone[4]), file=file)
        print("\t<span itemprop=\"image\">%s</span>" % (phone[14]), file=file)
        print("\t<div itemprop=\"brand\" itemscope itemtype=\"https://schema.org/Brand\">", file=file)
        print("\t\t<span itemprop=\"name\">%s</span>" % (phone[15]), file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">System Kernel</span>", file=file)
        print("\t\t<span itemprop=\"value\">%s</span>" % (phone[3]), file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Operating System</span>", file=file)
        print("\t\t<span itemprop=\"value\">%s</span>" % (phone[5]), file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Resolution</span>", file=file)
        print("\t\t<span itemprop=\"value\">%s</span>" % (phone[6]), file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Processor frequency</span>", file=file)
        print("\t\t<span itemprop=\"value\">%.2f</span>" % (phone[7]), file=file)
        print("\t\t<meta itemprop=\"unitCode\" content=\"A86\">Ghz", file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Kernel number</span>", file=file)
        print("\t\t<span itemprop=\"value\">%d</span>" % (phone[8]), file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">RAM capacity</span>", file=file)
        print("\t\t<span itemprop=\"value\">%d</span>" % (phone[9]), file=file)
        print("\t\t<meta itemprop=\"unitCode\" content=\"E34\">GB", file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">ROM capacity</span>", file=file)
        print("\t\t<span itemprop=\"value\">%d</span>" % (phone[10]), file=file)
        print("\t\t<meta itemprop=\"unitCode\" content=\"E34\">GB", file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Battery capacity</span>", file=file)
        print("\t\t<span itemprop=\"value\">%d</span>" % (phone[11]), file=file)
        print("\t\t<meta itemprop=\"unitCode\" content=\"MAH\">mAh", file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Rear camera pixels</span>", file=file)
        print("\t\t<span itemprop=\"value\">%d</span>" % (phone[12]), file=file)
        print("\t\t<meta itemprop=\"unitCode\" content=\"E38\">megapixel", file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Front camera pixels</span>", file=file)
        print("\t\t<span itemprop=\"value\">%d</span>" % (phone[13]), file=file)
        print("\t\t<meta itemprop=\"unitCode\" content=\"E38\">megapixel", file=file)
        print("\t</div>", file=file)
        print("\t<div itemprop=\"additionalProperty\" itemscope itemtype=\"https://schema.org/PropertyValue\">", file=file)
        print("\t\t<span itemprop=\"name\">Usage</span>", file=file)
        print("\t\t<span itemprop=\"value\">%s</span>" % (phone[16]), file=file)
        print("\t</div>", file=file)
        print("</div>", file=file)


phones = [[1, 'OPPO A32(8GB/128GB/ All Netcom )', 1499, 'Android', 6.5, 'Color', '720P', 1.8, 8, 8, 128, 5000, 13, 8,
           'https://pro-fd.zol-img.com.cn/t_s300x300c5/g6/M00/02/01/ChMkKV9Z_KeIBXZUAAC-BeJRWEUAACIDwEB6AoAAL4d919.jpg',
           'OPPO', 'Business'],
          [1, 'Redmi 8A(3GB/32GB/ All Netcom )', 599, 'MIUI', 6.22, 'MIUI', '720P', 2, 8, 3, 32, 5000, 12, 8,
           'https://pro-fd.zol-img.com.cn/t_s300x300c5/g1/M09/00/08/ChMljV2kSqWIUHBLAACcAbMG0LMAAP92QKihe4AAJwZ139.jpg',
           'Redmi', 'Business']]
exportJSON_LD(phones)
exportXML(phones)