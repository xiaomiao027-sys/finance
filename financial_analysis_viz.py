#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Financial Product Analysis Visualization
金融产品分析可视化脚本
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# 设置字体
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 设置样式
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8')

class FinancialAnalyzer:
    """Financial Product Analyzer"""
    
    def __init__(self):
        self.data = {}
        self.colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    def generate_sample_data(self):
        """Generate sample financial data"""
        np.random.seed(42)
        
        # Generate stock data
        dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D')
        n_days = len(dates)
        
        # Simulate stock price data
        initial_price = 100
        returns = np.random.normal(0.0008, 0.02, n_days)  # 日收益率
        prices = [initial_price]
        
        for ret in returns[1:]:
            prices.append(prices[-1] * (1 + ret))
        
        self.data['stock'] = pd.DataFrame({
            'Date': dates,
            'Price': prices,
            'Returns': returns,
            'Volume': np.random.randint(1000000, 5000000, n_days)
        })
        
        # Generate fund data
        self.data['funds'] = pd.DataFrame({
            'Fund_Type': ['Equity', 'Bond', 'Balanced', 'Money Market', 'Index'],
            'Annual_Return': [0.152, 0.042, 0.089, 0.028, 0.118],
            'Volatility': [0.225, 0.035, 0.145, 0.008, 0.198],
            'Sharpe_Ratio': [0.68, 1.20, 0.61, 3.50, 0.60],
            'Max_Drawdown': [-0.328, -0.021, -0.185, -0.002, -0.285]
        })
        
        # Generate portfolio allocation data
        self.data['portfolio'] = pd.DataFrame({
            'Asset_Class': ['Stocks', 'Bonds', 'Cash', 'Commodities', 'REITs'],
            'Weight': [0.45, 0.35, 0.10, 0.05, 0.05],
            'Expected_Return': [0.08, 0.04, 0.02, 0.06, 0.07],
            'Risk_Contribution': [0.65, 0.20, 0.02, 0.08, 0.05]
        })
        
        # Generate sector data
        self.data['sectors'] = pd.DataFrame({
            'Sector': ['Technology', 'Consumer', 'Financial', 'Healthcare', 'Energy', 'Industrial'],
            'Market_Cap': [15.2, 12.8, 18.5, 8.9, 6.3, 10.1],
            'PE_Ratio': [28.5, 22.3, 8.9, 35.2, 12.8, 16.7],
            'Dividend_Yield': [0.8, 2.1, 3.2, 1.2, 4.5, 2.3]
        })
    
    def plot_stock_performance(self):
        """Plot stock performance charts"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Stock Market Analysis', fontsize=16, fontweight='bold')
        
        # Stock price trend
        axes[0, 0].plot(self.data['stock']['Date'], self.data['stock']['Price'], 
                       color=self.colors[0], linewidth=1)
        axes[0, 0].set_title('Stock Price Trend')
        axes[0, 0].set_ylabel('Price')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Returns distribution
        axes[0, 1].hist(self.data['stock']['Returns'], bins=50, 
                       color=self.colors[1], alpha=0.7, edgecolor='black')
        axes[0, 1].set_title('Daily Returns Distribution')
        axes[0, 1].set_xlabel('Returns')
        axes[0, 1].set_ylabel('Frequency')
        axes[0, 1].axvline(self.data['stock']['Returns'].mean(), 
                          color='red', linestyle='--', label='Mean')
        axes[0, 1].legend()
        
        # Trading volume
        axes[1, 0].bar(self.data['stock']['Date'][-100:], 
                      self.data['stock']['Volume'][-100:], 
                      color=self.colors[2], alpha=0.7)
        axes[1, 0].set_title('Trading Volume (Last 100 days)')
        axes[1, 0].set_ylabel('Volume')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Cumulative returns
        cumulative_returns = (1 + self.data['stock']['Returns']).cumprod()
        axes[1, 1].plot(self.data['stock']['Date'], cumulative_returns, 
                       color=self.colors[3], linewidth=2)
        axes[1, 1].set_title('Cumulative Returns')
        axes[1, 1].set_ylabel('Cumulative Returns')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('c:/Users/64919/henry.github.io/docs/images/stock_performance.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_fund_comparison(self):
        """Plot fund comparison charts"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Fund Product Comparison Analysis', fontsize=16, fontweight='bold')
        
        # Risk-return scatter plot
        scatter = axes[0, 0].scatter(self.data['funds']['Volatility'], 
                                   self.data['funds']['Annual_Return'],
                                   s=self.data['funds']['Sharpe_Ratio']*100,
                                   c=self.colors[:len(self.data['funds'])],
                                   alpha=0.7)
        axes[0, 0].set_xlabel('Volatility')
        axes[0, 0].set_ylabel('Annual Return')
        axes[0, 0].set_title('Risk-Return Characteristics')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Add labels
        for i, fund in enumerate(self.data['funds']['Fund_Type']):
            axes[0, 0].annotate(fund, 
                              (self.data['funds']['Volatility'][i], 
                               self.data['funds']['Annual_Return'][i]),
                              xytext=(5, 5), textcoords='offset points')
        
        # Sharpe ratio comparison
        bars = axes[0, 1].bar(self.data['funds']['Fund_Type'], 
                             self.data['funds']['Sharpe_Ratio'],
                             color=self.colors[:len(self.data['funds'])])
        axes[0, 1].set_title('Sharpe Ratio Comparison')
        axes[0, 1].set_ylabel('Sharpe Ratio')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Add value labels
        for bar, value in zip(bars, self.data['funds']['Sharpe_Ratio']):
            axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                          f'{value:.2f}', ha='center', va='bottom')
        
        # Maximum drawdown comparison
        axes[1, 0].bar(self.data['funds']['Fund_Type'], 
                      self.data['funds']['Max_Drawdown'],
                      color=self.colors[:len(self.data['funds'])])
        axes[1, 0].set_title('Maximum Drawdown Comparison')
        axes[1, 0].set_ylabel('Maximum Drawdown')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Fund type distribution pie chart
        axes[1, 1].pie(self.data['funds']['Annual_Return'], 
                      labels=self.data['funds']['Fund_Type'],
                      colors=self.colors[:len(self.data['funds'])],
                      autopct='%1.1f%%')
        axes[1, 1].set_title('Fund Return Distribution')
        
        plt.tight_layout()
        plt.savefig('c:/Users/64919/henry.github.io/docs/images/fund_comparison.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_portfolio_analysis(self):
        """Plot portfolio analysis charts"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Portfolio Analysis', fontsize=16, fontweight='bold')
        
        # Asset allocation pie chart
        axes[0, 0].pie(self.data['portfolio']['Weight'], 
                      labels=self.data['portfolio']['Asset_Class'],
                      colors=self.colors[:len(self.data['portfolio'])],
                      autopct='%1.1f%%')
        axes[0, 0].set_title('Asset Allocation')
        
        # Expected return comparison
        bars = axes[0, 1].bar(self.data['portfolio']['Asset_Class'], 
                             self.data['portfolio']['Expected_Return'],
                             color=self.colors[:len(self.data['portfolio'])])
        axes[0, 1].set_title('Expected Return by Asset Class')
        axes[0, 1].set_ylabel('Expected Return')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Add value labels
        for bar, value in zip(bars, self.data['portfolio']['Expected_Return']):
            axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                          f'{value:.1%}', ha='center', va='bottom')
        
        # Risk contribution
        axes[1, 0].bar(self.data['portfolio']['Asset_Class'], 
                      self.data['portfolio']['Risk_Contribution'],
                      color=self.colors[:len(self.data['portfolio'])])
        axes[1, 0].set_title('Risk Contribution')
        axes[1, 0].set_ylabel('Risk Contribution')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Efficient frontier
        portfolios = np.random.multivariate_normal([0.08, 0.12], 
                                                 [[0.01, 0.005], [0.005, 0.02]], 
                                                 100)
        
        axes[1, 1].scatter(portfolios[:, 1], portfolios[:, 0], 
                          alpha=0.5, c='blue', s=20)
        axes[1, 1].scatter(0.12, 0.08, color='red', s=100, 
                          marker='*', label='Optimal Portfolio')
        axes[1, 1].set_xlabel('Volatility')
        axes[1, 1].set_ylabel('Expected Return')
        axes[1, 1].set_title('Efficient Frontier')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('c:/Users/64919/henry.github.io/docs/images/portfolio_analysis.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_sector_analysis(self):
        """Plot sector analysis charts"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Sector Analysis', fontsize=16, fontweight='bold')
        
        # Market cap distribution
        axes[0, 0].pie(self.data['sectors']['Market_Cap'], 
                      labels=self.data['sectors']['Sector'],
                      colors=self.colors[:len(self.data['sectors'])],
                      autopct='%1.1f%%')
        axes[0, 0].set_title('Market Cap Distribution')
        
        # PE ratio comparison
        bars = axes[0, 1].bar(self.data['sectors']['Sector'], 
                             self.data['sectors']['PE_Ratio'],
                             color=self.colors[:len(self.data['sectors'])])
        axes[0, 1].set_title('P/E Ratio Comparison')
        axes[0, 1].set_ylabel('P/E Ratio')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Add value labels
        for bar, value in zip(bars, self.data['sectors']['PE_Ratio']):
            axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                          f'{value:.1f}', ha='center', va='bottom')
        
        # Dividend yield
        axes[1, 0].bar(self.data['sectors']['Sector'], 
                      self.data['sectors']['Dividend_Yield'],
                      color=self.colors[:len(self.data['sectors'])])
        axes[1, 0].set_title('Dividend Yield Comparison')
        axes[1, 0].set_ylabel('Dividend Yield (%)')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Market cap vs PE ratio scatter plot
        scatter = axes[1, 1].scatter(self.data['sectors']['Market_Cap'], 
                                   self.data['sectors']['PE_Ratio'],
                                   s=self.data['sectors']['Dividend_Yield']*50,
                                   c=range(len(self.data['sectors'])),
                                   cmap='viridis',
                                   alpha=0.7)
        axes[1, 1].set_xlabel('Market Cap (Trillion)')
        axes[1, 1].set_ylabel('P/E Ratio')
        axes[1, 1].set_title('Market Cap vs Valuation')
        axes[1, 1].grid(True, alpha=0.3)
        
        # Add labels
        for i, sector in enumerate(self.data['sectors']['Sector']):
            axes[1, 1].annotate(sector, 
                              (self.data['sectors']['Market_Cap'][i], 
                               self.data['sectors']['PE_Ratio'][i]),
                              xytext=(5, 5), textcoords='offset points')
        
        plt.tight_layout()
        plt.savefig('c:/Users/64919/henry.github.io/docs/images/sector_analysis.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_summary_chart(self):
        """Create summary chart"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Financial Product Analysis Summary', fontsize=16, fontweight='bold')
        
        # Fund annual return comparison
        bars = axes[0, 0].bar(self.data['funds']['Fund_Type'], 
                             self.data['funds']['Annual_Return'],
                             color=self.colors[:len(self.data['funds'])])
        axes[0, 0].set_title('Fund Annual Return Comparison')
        axes[0, 0].set_ylabel('Annual Return')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        for bar, value in zip(bars, self.data['funds']['Annual_Return']):
            axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                          f'{value:.1%}', ha='center', va='bottom')
        
        # Asset allocation
        axes[0, 1].pie(self.data['portfolio']['Weight'], 
                      labels=self.data['portfolio']['Asset_Class'],
                      colors=self.colors[:len(self.data['portfolio'])],
                      autopct='%1.1f%%')
        axes[0, 1].set_title('Recommended Asset Allocation')
        
        # Sector market cap
        axes[1, 0].bar(self.data['sectors']['Sector'], 
                      self.data['sectors']['Market_Cap'],
                      color=self.colors[:len(self.data['sectors'])])
        axes[1, 0].set_title('Sector Market Cap Distribution')
        axes[1, 0].set_ylabel('Market Cap (Trillion)')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Risk-return scatter plot
        axes[1, 1].scatter(self.data['funds']['Volatility'], 
                          self.data['funds']['Annual_Return'],
                          s=self.data['funds']['Sharpe_Ratio']*100,
                          c=self.colors[:len(self.data['funds'])],
                          alpha=0.7)
        axes[1, 1].set_xlabel('Volatility')
        axes[1, 1].set_ylabel('Annual Return')
        axes[1, 1].set_title('Risk-Return Characteristics')
        axes[1, 1].grid(True, alpha=0.3)
        
        for i, fund in enumerate(self.data['funds']['Fund_Type']):
            axes[1, 1].annotate(fund, 
                              (self.data['funds']['Volatility'][i], 
                               self.data['funds']['Annual_Return'][i]),
                              xytext=(5, 5), textcoords='offset points')
        
        plt.tight_layout()
        plt.savefig('c:/Users/64919/henry.github.io/docs/images/financial_summary.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_all_visualizations(self):
        """Generate all visualization charts"""
        print("Generating financial analysis visualizations...")
        
        # Ensure directory exists
        import os
        os.makedirs('c:/Users/64919/henry.github.io/docs/images', exist_ok=True)
        
        # Generate data
        self.generate_sample_data()
        
        # Generate charts
        self.plot_stock_performance()
        self.plot_fund_comparison()
        self.plot_portfolio_analysis()
        self.plot_sector_analysis()
        self.create_summary_chart()
        
        print("Visualization charts generated successfully!")
        print("Files saved to:")
        print("- c:/Users/64919/henry.github.io/docs/images/stock_performance.png")
        print("- c:/Users/64919/henry.github.io/docs/images/fund_comparison.png")
        print("- c:/Users/64919/henry.github.io/docs/images/portfolio_analysis.png")
        print("- c:/Users/64919/henry.github.io/docs/images/sector_analysis.png")
        print("- c:/Users/64919/henry.github.io/docs/images/financial_summary.png")

def main():
    """Main function"""
    analyzer = FinancialAnalyzer()
    analyzer.generate_all_visualizations()

if __name__ == "__main__":
    main()
