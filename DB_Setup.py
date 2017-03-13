from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import Boolean, Date, Float, BigInteger

Base = declarative_base()

class FullMarketDailyTrade(Base):
    __tablename__ = 'fullmarketdailytrade'

    id = Column(Integer, primary_key = True)
    tradeDate = Column(Date(), unique = True)
    tradeVolume = Column(Integer)
    tradeValue = Column(Integer)
    transaction = Column(Integer)
    TAIEX = Column(Float())
    change = Column(Float())

class SingleStockDaily(Base):
    __tablename__ = 'singlestockdaily'
    
    id = Column(Integer, primary_key = True)
    tradeDate = Column(Date())
    tradeVolume = Column(BigInteger)
    tradeValue = Column(BigInteger)
    openingprice = Column(Float())
    highestprice = Column(Float())
    lowestprice = Column(Float())
    closingtprice = Column(Float())
    change = Column(Float())
    transaction = Column(Integer)
    stockid = Column(Integer)

engine = create_engine('sqlite:///taiwanstock.db')
Base.metadata.create_all(engine)