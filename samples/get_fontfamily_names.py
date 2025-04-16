from powcd2d.dwrite import DWRITE_FACTORY_TYPE, DWriteFactory

factory = DWriteFactory.create(DWRITE_FACTORY_TYPE.SHARED)
sysfontcol = factory.systemfontcollection
fontfamilies = sysfontcol.fontfamilies
for fontfamily in fontfamilies:
    print(fontfamily.familynames.strings)
