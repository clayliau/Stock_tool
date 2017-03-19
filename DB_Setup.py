from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.types import Boolean, Date, Float

Base = declarative_base()

class FullMarketDailyTrade(Base):
    __tablename__ = 'fullmarketdailytrade'

    id = Column(Integer, primary_key = True)
    tradeDate = Column(Date(), unique = True)
    tradeVolume = Column(Float())
    tradeValue = Column(Float())
    transaction = Column(Integer)
    TAIEX = Column(Float())
    change = Column(Float())
    avg5d = Column(Float())
    avg10d = Column(Float())
    avg20d = Column(Float())
    avg30d = Column(Float())
    avg60d = Column(Float())

class StockNameID(Base):
    __tablename__ = 'stocknameid'
    id = Column(Integer, primary_key = True)
    stockid = Column(String(10), unique = True)
    stockname = Column(String(30), unique = True)

class SingleStockDaily(Base):
    __tablename__ = 'singlestockdaily'
    
    id = Column(Integer, primary_key = True)
    tradeDate = Column(Date())
    tradeVolume = Column(Float())
    tradeValue = Column(Float())
    openingprice = Column(Float())
    highestprice = Column(Float())
    lowestprice = Column(Float())
    closingtprice = Column(Float())
    change = Column(Float())
    transaction = Column(Integer)
    stockid = Column(String(10), ForeignKey('stocknameid.stockid'))
    avg5d = Column(Float())
    avg10d = Column(Float())
    avg20d = Column(Float())
    avg30d = Column(Float())
    avg60d = Column(Float())
    stocknameid = relationship(StockNameID)

    def checkUnique(self, session, checkList):
        return session.query(SingleStockDaily).filter(SingleStockDaily.tradeDate==checkList[0],SingleStockDaily.stockid==checkList[1]).first()

engine = create_engine('sqlite:///taiwanstock.db')
Base.metadata.create_all(engine)